using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Essentials;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using M2Mqtt;
using M2Mqtt.Messages;

namespace Graduation_Project
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class Control : ContentPage
    {

        MqttClient mqttClient;
        static string broker = "test.mosquitto.org";
        static string topic = "GraduationProject/Implementation/Louay&Doreid";
        string message;
        bool clicked = true;
        bool clicked2 = true;

        public Control()
        {
            InitializeComponent();

            Task.Run(() =>
            {
                mqttClient = new MqttClient(broker);

                mqttClient.MqttMsgPublishReceived += MqttClient_MqttMsgPublishReceived;

                string clientId = Guid.NewGuid().ToString();

                mqttClient.Connect(clientId);

                mqttClient.Subscribe(new string[] { topic }, new byte[] { MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE });
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("0"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
            });

            
        }

        private void MqttClient_MqttMsgPublishReceived(object sender, MqttMsgPublishEventArgs e)
        {
            message = System.Text.Encoding.Default.GetString(e.Message);
        }

        private void forward_Pressed(object sender, EventArgs e)
        {
            if (message == "0")
            {
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("forward"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
                
            }
        }

        private void forward_Clicked(object sender, EventArgs e)
        {
            if (message == "forward")
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("0"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
        }

        private void left_Pressed(object sender, EventArgs e)
        {
            if (message == "0") { 
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("left"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
            }
        }

        private void left_Clicked(object sender, EventArgs e)
        {
            if (message == "left")
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("0"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
        }

        private void back_Pressed(object sender, EventArgs e)
        {
            if (message == "0")
            {
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("back"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
            }
               
        }

        private void back_Clicked(object sender, EventArgs e)
        {
            if (message == "back")
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("0"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
        }

        private void right_Pressed(object sender, EventArgs e)
        {
            if (message == "0")
            {
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("right"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
            }
                
        }

        private void right_Clicked(object sender, EventArgs e)
        {
            if (message == "right")
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("0"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
        }

        private async void RetractBtn_Clicked(object sender, EventArgs e)
        {
            if (clicked)
            {
                await RetractBtn.RotateTo(360);
                await Task.WhenAll(
                    controlLayout.TranslateTo(0, 300),
                    frame.TranslateTo(0, 300)
                    );
                clicked = false;
            }
            else
            {
                await RetractBtn.RotateTo(180);
                await Task.WhenAll(
                    controlLayout.TranslateTo(0, 0),
                    frame.TranslateTo(0, 0)
                    );
                clicked = true;
            }
            
            
        }

        private async void Back_Clicked_1(object sender, EventArgs e)
        {
            await Back.ScaleTo(0.8);
            await Back.ScaleTo(1);
            App.Current.MainPage = new Connected();
        }

        private void left2_Clicked(object sender, EventArgs e)
        {
            if (message == "yaw_left")
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("0"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
        }

        private void left2_Pressed(object sender, EventArgs e)
        {
            if (message == "0")
            {
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("yaw_left"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
            }
        }

        private void back2_Clicked(object sender, EventArgs e)
        {
            if (message == "pitch_up")
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("0"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
        }

        private void back2_Pressed(object sender, EventArgs e)
        {
            if (message == "0")
            {
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("pitch_up"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
            }
        }

        private void forward2_Clicked(object sender, EventArgs e)
        {
            if (message == "pitch_down")
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("0"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
        }

        private void forward2_Pressed(object sender, EventArgs e)
        {
            if (message == "0")
            {
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("pitch_down"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
            }
        }

        private void right2_Clicked(object sender, EventArgs e)
        {
            if (message == "yaw_right")
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("0"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
        }

        private void right2_Pressed(object sender, EventArgs e)
        {
            if (message == "0")
            {
                mqttClient.Publish(topic, Encoding.UTF8.GetBytes("yaw_right"), MqttMsgBase.QOS_LEVEL_AT_LEAST_ONCE, true);
            }
        }

        private async void RetractBtn2_Clicked(object sender, EventArgs e)
        {
            if (clicked2)
            {
                await RetractBtn2.RotateTo(180);
                await Task.WhenAll(
                    controlLayout2.TranslateTo(0, -300),
                    frame2.TranslateTo(0, -300)
                    );
                clicked2 = false;
            }
            else
            {
                await RetractBtn2.RotateTo(0);
                await Task.WhenAll(
                    controlLayout2.TranslateTo(0, 0),
                    frame2.TranslateTo(0, 0)
                    );
                clicked2 = true;
            }
        }
    }
}