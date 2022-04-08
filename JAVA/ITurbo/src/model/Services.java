
package model;

/**
 *
 * @author ITurbo
 */
public class Services {
      private String service_ID;
      private String service_name;
      private Employees employee;
      private double price;
      private Cabins cabin;

      public String getService_ID() {
            return service_ID;
      }

      public String getService_name() {
            return service_name;
      }

      public Employees getEmployee() {
            return employee;
      }

      public double getPrice() {
            return price;
      }

      public Cabins getCabin() {
            return cabin;
      }

      @Override
      public String toString() {
            return "Services{" + "service_ID=" + service_ID + ", service_name=" + service_name + ", employee=" + employee + ", price=" + price + ", cabin=" + cabin + '}';
      }
      
}
