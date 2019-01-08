#prime
import java.util.*;
public class Prime_not 
{
public static void main(String[] args) 
{
Scanner scan=new Scanner(System.in);
int num=scan.nextInt();
boolean flag = false;
for(int i = 2; i <= num/2; ++i)
{
if(num % i == 0)
{
flag = true;
break;
}
}
if (!flag)
System.out.println("yes");
else
System.out.println("no");
}
