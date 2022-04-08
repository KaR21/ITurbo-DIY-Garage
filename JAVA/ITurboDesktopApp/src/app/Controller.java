package app;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JOptionPane;

/**
 *
 * @author ITurbo
 */
public class Controller implements ActionListener {

      private Model model;
      private View view;

      public Controller(Model model, View view) {
            this.model = model;
            this.view = view;
            gehituActionListener(this);
      }

      private void gehituActionListener(ActionListener listener) {
            //GUIaren konponente guztiei gehitu listenerra
            view.jMenuItemAbout.addActionListener(listener);
            view.jMenuItemAmount.addActionListener(listener);
            view.jMenuItemFacturation.addActionListener(listener);
            view.jMenuItemMostUsed.addActionListener(listener);
            view.jMenuItemTodays.addActionListener(listener);
      }

      @Override
      public void actionPerformed(ActionEvent e) {
            String actionCommand = e.getActionCommand();
            //listenerrak entzun dezakeen eragiketa bakoitzeko. Konponenteek 'actionCommad' propietatea daukate
            switch (actionCommand) {
                  case "TO":
                        model.TodaysOccupationInit(view);
                        break;
                  case "FACTU":
                        model.FacturationInit(view);
                        break;
                  case "MUS":
                        model.MostusedInit(view);
                        break;
                  case "AOC":
                        model.AmountofcustomersInit(view);
                        break;
                  case "ABOUT":
                        JOptionPane.showMessageDialog(null, "Developed by: ITurbo\n Contact: iturbo@gmail.com", "About", JOptionPane.INFORMATION_MESSAGE);
                        break;
            }
      }
}
