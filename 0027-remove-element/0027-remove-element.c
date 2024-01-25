int removeElement(int* nums, int numsSize, int val){
  int a[900],c=0;
  int k=0;
  for(int i =0;i<numsSize;i++)
  {
    if(nums[i]!=val)
    {
      a[c]=nums[i];
      k++;
      c++;
    }

  }
  for(int i=0;i<k;i++){
    nums[i]=a[i];
  }
  return k;
}