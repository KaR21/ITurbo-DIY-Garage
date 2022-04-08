
package model;

/**
 *
 * @author ITurbo
 */
public class Managers {
      private String manager_ID;
      private String man_name;
      private String man_surname;
      private String email;
      private String position;

      public String getManager_ID() {
            return manager_ID;
      }

      public String getMan_name() {
            return man_name;
      }

      public String getMan_surname() {
            return man_surname;
      }

      public String getEmail() {
            return email;
      }

      public String getPosition() {
            return position;
      }

      @Override
      public String toString() {
            return "Managers{" + "manager_ID=" + manager_ID + ", man_name=" + man_name + ", man_surname=" + man_surname + ", email=" + email + ", position=" + position + '}';
      }
      
}
