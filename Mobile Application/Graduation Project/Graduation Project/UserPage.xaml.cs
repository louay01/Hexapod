using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using M2Mqtt;
using M2Mqtt.Messages;
using M2Mqtt.Session;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace Graduation_Project
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class UserPage : ContentPage
    {
        bool connected = false;
        MqttClient mqttClient;
        static string broker = "test.mosquitto.org";
        static string topic = "GraduationProject/Implementation/Louay&Doreid";

        public UserPage()
        {
            InitializeComponent();

            Task.Run(() =>
            {
                mqttClient = new MqttClient(broker);

                mqttClient.MqttMsgPublishReceived += MqttClient_MqttMsgPublishReceived;

                string clientId = Guid.NewGuid().ToString();

                mqttClient.Connect(clientId);

                mqttClient.Subscribe(new string[] { topic }, new byte[] { MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE });
            });
        }

        private void MqttClient_MqttMsgPublishReceived(object sender, MqttMsgPublishEventArgs e)
        {
            var message = System.Text.Encoding.Default.GetString(e.Message);
            if (message == "Marhaba_Back")
            {
                connected = true;
                Device.BeginInvokeOnMainThread(() =>
                {
                    
                });
            }
        }

        private void LogOutBtn_Clicked(object sender, EventArgs e)
        {
            App.Current.MainPage = new MainPage();
        }

        private async void RefreshBtn_Clicked(object sender, EventArgs e)
        {
            mqttClient.Publish(topic, Encoding.UTF8.GetBytes("Marhaba"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
            await RefreshBtn.RotateTo(360);
            await RefreshBtn.RotateTo(0);
            if (connected)
            {
                RefreshBtn.IsVisible = false;
                NoRobots.IsVisible = false;
                RobotAvailable.IsVisible = true;
                ConnectBtn.IsVisible = true;
            }
        }

        private void ConnectBtn_Clicked(object sender, EventArgs e)
        {
            App.Current.MainPage = new Connected();
        }
    }
}