public class hologram {
    public hologram() {
    }
 
    public static void main(String[] var0) {
       for(int var1 = 0; var1 < 5; ++var1) {
          for(int var2 = 0; var2 <= var1; ++var2) {
             if (var1 != 0 && var2 != 0 && var1 != 4 && var2 != var1) {
                System.out.print(" ");
             } else {
                System.out.print("*");
             }
          }
 
          System.out.println();
       }
 
    }
 }
 /*
  **
  * *
  *  * 
  *****  

  */