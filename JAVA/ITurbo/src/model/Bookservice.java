
package model;

import java.time.LocalDate;

/**
 *
 * @author ITurbo
 */
public class Bookservice {
      private String serviceBooked_ID;
      private Services service;
      private Customers customer;
      private LocalDate date;
      private LocalDate hour;

      public String getServiceBooked_ID() {
            return serviceBooked_ID;
      }

      public Services getService() {
            return service;
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
            return "Bookservice{" + "serviceBooked_ID=" + serviceBooked_ID + ", service=" + service + ", customer=" + customer + ", date=" + date + ", hour=" + hour + '}';
      }
      
}
