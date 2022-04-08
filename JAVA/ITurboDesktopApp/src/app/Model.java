package app;

import app.Amountofcustomers;
import app.Facturation;
import app.Mostused;
import app.TodaysOccupation;
import app.View;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 *
 * @author ITurbo
 */
public class Model {

      private TodaysOccupation to;
      private Facturation fa;
      private Mostused mus;
      private Amountofcustomers aoc;

      private static final String DB = "db/ITurbo.db";

      void TodaysOccupationInit(View view) {
            view.jPanel.setVisible(true);
            if (to == null || to.isClosed()) { //to not open several times if its open already
                  to = new TodaysOccupation();
                  view.jPanel.add(to);
                  to.show();
            }
      }

      void FacturationInit(View view) {
            view.jPanel.setVisible(true);
            if (fa == null || fa.isClosed()) { //to not open several times if its open already
                  fa = new Facturation();
                  view.jPanel.add(fa);
                  fa.show();
            }
      }

      void MostusedInit(View view) {
            view.jPanel.setVisible(true);
            if (mus == null || mus.isClosed()) { //to not open several times if its open already
                  mus = new Mostused();
                  view.jPanel.add(mus);
                  mus.show();
            }
      }

      void AmountofcustomersInit(View view) {
            view.jPanel.setVisible(true);
            if (aoc == null || aoc.isClosed()) { //to not open several times if its open already
                  aoc = new Amountofcustomers();
                  view.jPanel.add(aoc);
                  aoc.show();
            }
      }

      public Connection connect() {
            Connection conn = null;
            String url = "jdbc:sqlite:" + DB;
            try {
                  conn = DriverManager.getConnection(url);

            } catch (SQLException e) {
                  System.out.println(e.getMessage());
            }
            return conn;
      }
}
