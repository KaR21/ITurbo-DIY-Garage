
package model;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
/**
 *
 * @author ITurbo
 */
public class Model {

      private static final String DB = "db/HiztegiaMCV.db";
      private static String taula;

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

      public void terminoakImprimatu() {
            String sql = "SELECT * FROM " + taula;

            try (Connection conn = this.connect();
                    Statement stmt = conn.createStatement();
                    ResultSet rs = stmt.executeQuery(sql)) {
                  System.out.println("Datu basearen izena " + DB + " izango da eta hurrengo datuak izango ditu:");
                  System.out.println("ID\tEUSKARAZ\tGAZTELERAZ");

                  while (rs.next()) {
                        System.out.printf(rs.getInt("id") + "\t"
                                + rs.getString("euskaraz") + "\t"
                                + rs.getString("gazteleraz") + "\n");
                  }
            } catch (SQLException e) {
                  System.out.println(e.getMessage());
            }
      }

      public void terminoaGehitu(String euskaraz, String gazteleraz) {
            String sql = "INSERT INTO " + taula + "(euskaraz,gazteleraz) VALUES(?,?)";
            try (Connection conn = this.connect(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
                  pstmt.setString(1, euskaraz);
                  pstmt.setString(2, gazteleraz);
                  pstmt.executeUpdate();
            } catch (SQLException e) {
                  System.out.println(e.getMessage());
            }
      }
       public void terminoaEzabatu(int id) {
        String sql = "DELETE FROM " + taula + " WHERE id = ?";

        try (Connection conn = this.connect();
                PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setInt(1, id);
            pstmt.executeUpdate();

        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
    
    
    public void terminoaAldatu(int id, String euskaraz, String gazteleraz) {
        String sql = "UPDATE " + taula + " SET euskaraz = ?, gazteleraz = ? WHERE id = ?";

        try (Connection conn = this.connect();
                PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setString(1, euskaraz);
            pstmt.setString(2, gazteleraz);
            pstmt.setInt(3, id);
            pstmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}
