package app;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.ArrayList;

public class LoginFrame extends JFrame implements ActionListener {

      private ArrayList<String> staffname = new ArrayList<String>();
      private ArrayList<String> staffpassword = new ArrayList<String>();

      Container container = getContentPane();
      JLabel userLabel = new JLabel("USERNAME");
      JLabel passwordLabel = new JLabel("PASSWORD");
      JTextField userTextField = new JTextField();
      JPasswordField passwordField = new JPasswordField();
      JButton loginButton = new JButton("LOGIN");
      JButton resetButton = new JButton("RESET");
      JCheckBox showPassword = new JCheckBox("Show Password");

      LoginFrame() {
            setUsers();
            setLayoutManager();
            setLocationAndSize();
            addComponentsToContainer();
            addActionEvent();

      }

      public void setUsers() {
            staffname.add("Joseba");
            staffpassword.add("4321");

            staffname.add("Karmele");
            staffpassword.add("1234");
      }

      public void setLayoutManager() {
            container.setLayout(null);
      }

      public void setLocationAndSize() {
            userLabel.setBounds(50, 150, 100, 30);
            passwordLabel.setBounds(50, 220, 100, 30);
            userTextField.setBounds(150, 150, 150, 30);
            passwordField.setBounds(150, 220, 150, 30);
            showPassword.setBounds(150, 250, 150, 30);
            loginButton.setBounds(50, 300, 100, 30);
            resetButton.setBounds(200, 300, 100, 30);

      }

      public void addComponentsToContainer() {
            container.add(userLabel);
            container.add(passwordLabel);
            container.add(userTextField);
            container.add(passwordField);
            container.add(showPassword);
            container.add(loginButton);
            container.add(resetButton);
      }

      public void addActionEvent() {
            loginButton.addActionListener(this);
            resetButton.addActionListener(this);
            showPassword.addActionListener(this);
      }

      @Override
      public void actionPerformed(ActionEvent e) {
            int i = 0;
            boolean found = false;
            
            if (e.getSource() == loginButton) {
                  String userText;
                  String pwdText;
                  userText = userTextField.getText();
                  pwdText = passwordField.getText();
                  if (userText.equalsIgnoreCase("Admin") && pwdText.equalsIgnoreCase("Admin123")) {
                        found = true;
                        //JOptionPane.showMessageDialog(this, "Login Successful");
                        this.dispose();
                        View view = View.viewCreate();

                        Model model = new Model();

                        Controller controller = new Controller(model, view);

                        view.setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE);
                        view.addWindowListener(new WindowAdapter() {
                              public void windowClosing(WindowEvent e) {
                                    String message = " Are you sure you want to exit ? ";
                                    String title = "Exit";
                                    int reply = JOptionPane.showConfirmDialog(null, message, title, JOptionPane.YES_NO_OPTION);
                                    if (reply == JOptionPane.YES_OPTION) {
                                          System.exit(0);
                                    }

                              }
                        });
                        view.setVisible(true);
                  } else {
                        while (i < staffname.size() && found == false) {
                              if (userText.equalsIgnoreCase(staffname.get(i)) && pwdText.equalsIgnoreCase(staffpassword.get(i))) {
                                    found = true;
                                    this.dispose();
                                    View view = View.viewCreate();

                                    Model model = new Model();

                                    Controller controller = new Controller(model, view);

                                    view.setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE);
                                    view.addWindowListener(new WindowAdapter() {
                                          public void windowClosing(WindowEvent e) {
                                                String message = " Are you sure you want to exit ? ";
                                                String title = "Exit";
                                                int reply = JOptionPane.showConfirmDialog(null, message, title, JOptionPane.YES_NO_OPTION);
                                                if (reply == JOptionPane.YES_OPTION) {
                                                      System.exit(0);
                                                }

                                          }
                                    });
                                    view.setVisible(true);
                              }
                              i++;
                                    
                        }
                        if(found == false){
                              JOptionPane.showMessageDialog(null, "INCORRECT PASSWORD OR USERNAME");
                        }
                        /*else{
                              JOptionPane.showMessageDialog(null, "Hello " + userText);
                        }*/
                  }
            }
            if (e.getSource() == resetButton) {
                  userTextField.setText("");
                  passwordField.setText("");
            }
            if (e.getSource() == showPassword) {
                  if (showPassword.isSelected()) {
                        passwordField.setEchoChar((char) 0);
                  } else {
                        passwordField.setEchoChar('*');
                  }

            }
      }

}
