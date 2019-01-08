import java.util.*;
public class Array_sum{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int k=sc.nextInt();
		int sum=0;
		int a[]=new int[n];
		for (int i = 0; i < a.length; i++) {
			a[i]=sc.nextInt();
		}
		for(int i=0;i<k;i++)
		{
			sum=sum+a[i];
		}
			System.out.println(sum);		
	}
}
