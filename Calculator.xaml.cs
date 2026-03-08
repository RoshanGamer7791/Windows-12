using System;
using System.Collections.Generic;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace Windows_12
{
    /// <summary>
    /// Interaction logic for Calculator.xaml
    /// </summary>
    public partial class Calculator : Window
    {
        public Calculator()
        {
            InitializeComponent();
        }

        private void Add(object sender, RoutedEventArgs e)
        {
            if (double.TryParse(Val1.Text, out double num1) && double.TryParse(Val2.Text, out double num2))
            {
                Ans.Text = (num1 + num2).ToString();
            }
            else
            {
                MessageBox.Show("Please enter valid numbers.", "Numbers", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void Subtract(object sender, RoutedEventArgs e)
        {
            if (double.TryParse(Val1.Text, out double num1) && double.TryParse(Val2.Text, out double num2))
            {
                Ans.Text = (num1 - num2).ToString();
            }
            else
            {
                MessageBox.Show("Please enter valid numbers.", "Numbers", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void Times(object sender, RoutedEventArgs e)
        {
            if (double.TryParse(Val1.Text, out double num1) && double.TryParse(Val2.Text, out double num2))
            {
                Ans.Text = (num1 * num2).ToString();
            }
            else
            {
                MessageBox.Show("Please enter valid numbers.", "Numbers", MessageBoxButton.OK, MessageBoxImage.Error);
            }
        }

        private void Divide(object sender, RoutedEventArgs e)
        {
            if (double.TryParse(Val1.Text, out double num1) && double.TryParse(Val2.Text, out double num2))
            {
                if (num2 != 0)
                {
                    Ans.Text = (num1 / num2).ToString();
                }
                else
                {
                    MessageBox.Show("Cannot divide by zero.", "Numbers", MessageBoxButton.OK, MessageBoxImage.Error);
                }
            }
            else
            {
                MessageBox.Show("Please enter valid numbers.", "Numbers", MessageBoxButton.OK, MessageBoxImage.Error);
            }

        }
    }
}