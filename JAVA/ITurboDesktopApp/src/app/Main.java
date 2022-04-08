package app;

import javax.swing.JFrame;

/**
 *
 * @author ITurbo
 */
public class Main {

      public static void main(String[] a) {
            LoginFrame frame = new LoginFrame();
            frame.setTitle("Login Form");
            frame.setVisible(true);
            frame.setBounds(500, 200, 370, 600);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setResizable(false);
            

      }
}
