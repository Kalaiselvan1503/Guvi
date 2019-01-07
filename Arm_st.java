#armstrong
import java.util.*;
public class Arm_st {
public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		 int c=0,a,temp;  
		    int n=sc.nextInt();
		    temp=n;  
		    while(n>0)  
		    {  
		    a=n%10;  
		    n=n/10;  
		    c=c+(a*a*a);  
		    }  
		    if(temp==c)  
		    System.out.println("yes");   
		    else  
		        System.out.println("no");   
	}
}
