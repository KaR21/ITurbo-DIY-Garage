
package model;

/**
 *
 * @author ITurbo
 */
public class Customers {
      private String id_Customer;
      private String cust_name;
      private String cust_surname;
      private int phone;
      private String email;

      public String getId_Customer() {
            return id_Customer;
      }

      public String getCust_name() {
            return cust_name;
      }

      public String getCust_surname() {
            return cust_surname;
      }

      public int getPhone() {
            return phone;
      }

      public String getEmail() {
            return email;
      }

      @Override
      public String toString() {
            return "Customers{" + "id_Customer=" + id_Customer + ", cust_name=" + cust_name + ", cust_surname=" + cust_surname + ", phone=" + phone + ", email=" + email + '}';
      }
      
}
