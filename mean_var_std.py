import numpy as np

def calculate(list):
  # print(len(list))
  # if len(list) >=9:
  # def fun(list):
  #   if len(list)<9:
  #     raise ValueError("List must contain nine numbers.")
  #   else:
  #     return True
  try :
    
    lista2=np.array(list)
    lista2=np.mean(lista2.reshape(3, 3))
    lista=np.array(list)
    lista.resize(9,1)
    ar= np.array(list)
    ar.resize(3, 3)

    dim=np.size(ar, 0)

    me_r=[]
    var_r=[]
    var_r2=[]
    ma_r=[]
    mi_r=[]
    su_r=[]
    for i in range(dim):
      me_r.append(np.mean(ar[:,i]))
      me=np.mean(ar[:,i])
      ma=np.max((ar[:,i]))
      mi=np.min((ar[:,i]))
      sig=sum((ar[:,i]-me)**2)/3
      sig2=sig**0.5
      var_r.append(sig)
      var_r2.append(sig2)
      ma_r.append(ma)
      mi_r.append(mi)
      su_r.append(sum(ar[:,i]))
      
    me_c=[]
    var_c=[]
    var_c2=[]
    ma_c=[]
    mi_c=[]
    su_c=[]
    for i in range(dim):
  
      me_c.append(np.mean(ar[i,:]))
      me=np.mean(ar[i,:])
      ma=np.max((ar[i,:]))
      mi=np.min((ar[i,:]))
      sig=sum((ar[i,:]-me)**2)/3
      sig2=sig**0.5
      var_c.append(sig)
      var_c2.append(sig2)
      ma_c.append(ma)
      mi_c.append(mi)
      su_c.append(sum(ar[i,:]))      
    me_a=np.mean(lista)
    sig_a=    np.var(lista)
    sig2_a=sig_a**0.5
    ma_a=np.max(lista)
    mi_a=np.min(lista)
    su_a=sum(sum(lista))
    me_f=[me_r,me_c,me_a]  
    var_f=[var_r,var_c,sig_a]   
    var_f2= [var_r2,var_c2,sig2_a]
    ma_f=[ma_r,ma_c,ma_a]
    mi_f=[mi_r,mi_c,mi_a]
    su_f=[su_r,su_c,su_a]
  
  
  
    calculations={ 'mean':me_f,'variance':var_f,'standard deviation':var_f2,'max':ma_f,'min':mi_f,'sum':su_f}
    return calculations
  except ValueError as err: 
    raise ValueError("List must contain nine numbers.") from err
    # err.args=list()
    # err.args=list("List must contain nine numbers.")
    # print(type(err.args))
    # err.args="".join("List must contain nine numbers.")
    # return (err)
    # ValueError("List must contain nine numbers.")
    # return (ValueError("List must contain nine numbers."))
  
  
    ## si es may a 9 tomara solo los 9 numeros primeros
    # return  calculations

    




  

# print(calculate([2,6,2,8,4,0,1,]))


# print(calculate([9,1,5,3,3,3,2,9,0]))

# expected = {'mean': [[4.666666666666667, 4.333333333333333, 2.6666666666666665], [5.0, 3.0, 3.6666666666666665], 3.888888888888889], 'variance': [[9.555555555555555, 11.555555555555557, 4.222222222222222], [10.666666666666666, 0.0, 14.888888888888891], 9.209876543209875], 'standard deviation': [[3.0912061651652345, 3.39934634239519, 2.0548046676563256], [3.265986323710904, 0.0, 3.8586123009300755], 3.0347778408328137], 'max': [[9, 9, 5], [9, 3, 9], 9], 'min': [[2, 1, 0], [1, 3, 0], 0], 'sum': [[14, 13, 8], [15, 9, 11], 35]}
# print(expected)




  

# actual =calculate([2,6,2,8,4,0,1,5,7])
# print(actual)

# expected = {'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889], 'variance': [[9.555555555555557, 0.6666666666666666, 8.666666666666666], [3.555555555555556, 10.666666666666666, 6.222222222222221], 6.987654320987654], 'standard deviation': [[3.091206165165235, 0.816496580927726, 2.943920288775949], [1.8856180831641267, 3.265986323710904, 2.494438257849294], 2.6434171674156266], 'max': [[8, 6, 7], [6, 8, 7], 8], 'min': [[1, 4, 0], [2, 0, 1], 0], 'sum': [[11, 15, 9], [10, 12, 13], 35]}
# # print(expected)
# # print(type(actual),type(expected))

# for key,value in actual.items():
#   print(actual[key],"------",expected[key])