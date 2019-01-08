import java.util.*;
class Prime_from1{
    public static void main(String[] args) {
          Scanner a=new Scanner(System.in);
          int n=a.nextInt();
          int q=a.nextInt();
          int f,i;
          while(n<q)
                  {
                      f=0;
                      for(i=2;i<=n/2;i++)
                      {
                          if(n%i==0)
                          {
                              f=1;
                              break;
                          }
                      }
                      if(f==0)
                      {
                          if(n==1)
                          {
                              
                          }
                          else
                          System.out.print(n+" ");
                      }
                      ++n;
                      
                  }
    }
    }
