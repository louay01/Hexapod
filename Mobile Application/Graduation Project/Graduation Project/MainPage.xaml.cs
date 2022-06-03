using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;
using M2Mqtt;
using M2Mqtt.Messages;

namespace Graduation_Project
{
    public partial class MainPage : ContentPage
    {
        static string username = "user";
        static string pass = "123";

        public MainPage()
        {
            InitializeComponent();
        }

        private void ConnectBtn_Clicked(object sender, EventArgs e)
        {
            //mqttClient.Publish(topic, Encoding.UTF8.GetBytes("Hello"));
            if (UserNameEntry.Text == username && PassEntry.Text == pass)
                App.Current.MainPage = new UserPage();
            else
                Wrong.IsVisible = true;
        }
    }
}
