
package model;

/**
 *
 * @author ITurbo
 */
public class Cabins {
      private String id_Cabin;
      private String cabin_name;
      private String description;
      private double surface;
      private double price;

      public String getId_Cabin() {
            return id_Cabin;
      }

      public String getCabin_name() {
            return cabin_name;
      }

      public String getDescription() {
            return description;
      }

      public double getSurface() {
            return surface;
      }

      public double getPrice() {
            return price;
      }

      @Override
      public String toString() {
            return "Cabins{" + "id_Cabin=" + id_Cabin + ", cabin_name=" + cabin_name + ", description=" + description + ", surface=" + surface + ", price=" + price + '}';
      }
      
}
