
package model;

import java.time.LocalDate;

/**
 *
 * @author ITurbo
 */
public class Bookcabin {
      private String cabinBooked_ID;
      private Cabins cabinID;
      private Customers customer;
      private LocalDate date;
      private LocalDate hour;

      public String getCabinBooked_ID() {
            return cabinBooked_ID;
      }

      public Cabins getCabinID() {
            return cabinID;
      }

      public Customers getCustomer() {
            return customer;
      }

      public LocalDate getDate() {
            return date;
      }

      public LocalDate getHour() {
            return hour;
      }

      @Override
      public String toString() {
            return "Bookcabin{" + "cabinBooked_ID=" + cabinBooked_ID + ", cabinID=" + cabinID + ", customer=" + customer + ", date=" + date + ", hour=" + hour + '}';
      }
      
}
