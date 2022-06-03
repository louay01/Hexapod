using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using M2Mqtt;
using M2Mqtt.Messages;
using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace Graduation_Project
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class Connected : ContentPage
    {
        
        public Connected()
        {
            InitializeComponent();
        }

        private void LogOutBtn_Clicked(object sender, EventArgs e)
        {
            App.Current.MainPage = new MainPage();
        }

        private void switch1_Toggled(object sender, ToggledEventArgs e)
        {
            if (switch1.IsToggled)
            {
                switch2.IsToggled = false;
                Mode.Text = "Automatic Mode";
            }
            else if (!switch2.IsToggled)
                Mode.Text = "Choose a Mode";

        }

        private void switch2_Toggled(object sender, ToggledEventArgs e)
        {
            if (switch2.IsToggled)
            {
                switch1.IsToggled = false;
                Mode.Text = "Manual Mode";
            }
            else if (!switch1.IsToggled)
                Mode.Text = "Choose a Mode";
        }

        private void StartBtn_Clicked(object sender, EventArgs e)
        {
            App.Current.MainPage = new Control();
        }
    }
}