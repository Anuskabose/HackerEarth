#include<stdio.h>
int main()
{
    int i,t;
    long long int a[4];
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        for(int j=0;j<4;j++)
          scanf("%lld",&a[j]);
        if(a[0]*a[1]==a[2]+a[3])
            printf("Yes\n");
        else
         printf("No\n");
    }
      return 0;

}
