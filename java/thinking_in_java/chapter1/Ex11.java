/** Exercise 11
* Turn the AllTheColorsOfTheRainbow example into
* a program that compiles and runs.
*/
public class Ex11 {
  int anIntegerRepresentingColors;
  void changeTheHueOfTheColor(int newHue) {
    anIntegerRepresentingColors = newHue;
  }

  public static void main(String[] args) {
    Ex11 rainbow = new Ex11();
    System.out.println(rainbow.anIntegerRepresentingColors);
    rainbow.changeTheHueOfTheColor(2);
    System.out.println(rainbow.anIntegerRepresentingColors);
  }
}