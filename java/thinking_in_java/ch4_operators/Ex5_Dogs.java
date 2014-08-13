/** Exercise 5
* Create a class called Dog with two Strings:
* name and says. In main(), create two dogs,
* "spot" who says, "Ruff!", and "scuffy" who
* says, "Wurf!". Then display their names and
* what they say.
*/
class Dog {
  String name;
  String says;

  public Dog(String name, String says) {
    this.name = name;
    this.says = says;
  }
}

public class Ex5_Dogs {
  public static void main(String[] args) {
    Dog spot = new Dog("spot", "Ruff!");
    Dog scruffy = new Dog("scruffy", "Wurf!");
    System.out.println(spot.name + " says " + spot.says);
    System.out.println(scruffy.name + " says " + scruffy.says);
  }  
}
