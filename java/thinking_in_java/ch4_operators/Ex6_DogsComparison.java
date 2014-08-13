/** Exercise 6
* Following Exercise 5 assign a new Dog
* reference to spot's object. test for comparison
* using == and equals() for all references.
*/
class Dog {
  String name;
  String says;

  public Dog(String name, String says) {
    this.name = name;
    this.says = says;
  }
}

public class Ex6_DogsComparison {
  public static void main(String[] args) {
    Dog dog1 = new Dog("spot", "ruff");
    Dog dog2 = new Dog("scruffy", "wurf");
    Dog dog1_clone = dog1;
    System.out.println("dog1 == dog1_clone : " + (dog1 == dog1_clone));
    System.out.println("dog1.equals(dog1_clone) : " + dog1.equals(dog1_clone));
    System.out.println("dog1_clone == dog2 : " + (dog1_clone == dog2));
    System.out.println("dog1_clone.equals(dog2) : " + dog1_clone.equals(dog2));
  }
}
