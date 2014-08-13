import java.util.*;

/** Exercise 12
* Find the code for the second version of HelloDate.java,
* the simple comment-document example. Execute Javadoc on the
* file and view the results with your Web browser.

* The program begins as follows.
* The first Thinking in Java example program.
* Displays a string and today's date.
* @author Anh Le
* @author www.anhqle.wordpress.com
* @version 4.0
*/
public class Ex12_LeftToReader {
  /** Entry point to class & application.
  * @params args array of string arguments
  * @throws exceptions No exceptions thrown
  */
  public static void main(String[] args) {
    System.out.println("Hello, it's: ");
    System.out.println(new Date());
  }
} /* Output: (55% match)
Hello, it's:
Today's date
*/

