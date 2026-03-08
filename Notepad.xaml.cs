using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using System.IO;
using Microsoft.Win32;

namespace Windows_12
{
    /// <summary>
    /// Interaction logic for Notepad.xaml
    /// </summary>
    public partial class Notepad : Window
    {
        public Notepad()
        {
            InitializeComponent();
        }

        private void Savefile(object sender, RoutedEventArgs e)
        {
            SaveFileDialog saveFileDialog = new SaveFileDialog();
            saveFileDialog.Filter = "Text file (*.txt)|*.txt|All files (*.*)|*.*";
            saveFileDialog.Title = "Save file";
            if (saveFileDialog.ShowDialog() == true)
            {
                File.WriteAllText(saveFileDialog.FileName, Textbox.Text);
                MessageBox.Show($"File saved successfully at {saveFileDialog.FileName}.", "Success", MessageBoxButton.OK, MessageBoxImage.Information);
            }
            else
            {
                MessageBox.Show("File not saved.", "Failed", MessageBoxButton.OK, MessageBoxImage.Error);
                return;
            }
        }

        private void Loadfile(object sender, RoutedEventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.Filter = "Text file (*.txt)|*.txt|All files (*.*)|*.*";
            openFileDialog.Title = "Open file";
            if (openFileDialog.ShowDialog() == true)
            {
                Textbox.Text = File.ReadAllText(openFileDialog.FileName);
                MessageBox.Show($"File loaded successfully from {openFileDialog.FileName}.", "Success", MessageBoxButton.OK, MessageBoxImage.Information);
            }
            else
            {
                MessageBox.Show("File not loaded.", "Failed", MessageBoxButton.OK, MessageBoxImage.Error);
                return;
            }
        }
    }
}
