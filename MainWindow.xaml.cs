using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Windows_12
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }
        bool startmenuopened = false;
        StartMenu StartMenu = new StartMenu();
        private void OpenStartMenu(object sender, RoutedEventArgs e)
        {
            if (startmenuopened)
            {
                StartMenuFrame.Content = null;
            }
            else
            {
                StartMenuFrame.Navigate(StartMenu);
            }
            startmenuopened = !startmenuopened;
        }
    }
}