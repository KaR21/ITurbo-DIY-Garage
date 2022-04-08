
package model;

/**
 *
 * @author ITurbo
 */
public class Employees {
      private String emp_ID;
      private String emp_name;
      private String emp_surname;
      private String email;
      private String position;

      public String getEmp_ID() {
            return emp_ID;
      }

      public String getEmp_name() {
            return emp_name;
      }

      public String getEmp_surname() {
            return emp_surname;
      }

      public String getEmail() {
            return email;
      }

      public String getPosition() {
            return position;
      }

      @Override
      public String toString() {
            return "Employees{" + "emp_ID=" + emp_ID + ", emp_name=" + emp_name + ", emp_surname=" + emp_surname + ", email=" + email + ", position=" + position + '}';
      }
      
      
}
