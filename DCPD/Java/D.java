public class D {
    public static void main(String[] args) {
        for(int i=0; i<5; i++)
		{
			for(int j=0; j<=5; j++)
			{
				if (j == 1 || ((i == 0 || i == 4) && 
               (j > 1 && j < 3)) || (j == 3 && 
                i != 0 && i != 4))
                {
                    System.out.print("*");
                }
                else{
                    System.out.print(" ");
                }
				 
				
				
			}
			System.out.println();

		}
    }
    
}
