# f = [5, 10, 15, 20, 25, 20, 15, 10, 5]
f = [1, 8, 28, 56, 70, 56, 28, 8, 1]
sum_fx = 0
N = sum(f)

# find fx
for x in range(len(f)):
    sum_fx += f[x] * x

# calclate mean
mean_ = sum_fx / N

# calculate f(x-mean)
sum_f_into_x_sub_mean = 0
sum_f_into_x_sub_mean_raise_2 = 0
sum_f_into_x_sub_mean_raise_3 = 0
sum_f_into_x_sub_mean_raise_4 = 0
for x in range(len(f)):
    sum_f_into_x_sub_mean += f[x] * (x - mean_)
    sum_f_into_x_sub_mean_raise_2 += (f[x] * ((x - mean_)**2))
    sum_f_into_x_sub_mean_raise_3 += (f[x] * ((x - mean_)**3))
    sum_f_into_x_sub_mean_raise_4 += (f[x] * ((x - mean_)**4))


# print(N, sum_f_into_x_sub_mean, sum_fx, mean_)

print('N = ', N)
print('summation of fx = ', sum_fx)
print('summation of f(x-mean) = ', sum_f_into_x_sub_mean)
print('summation of f(x-mean)^2 = ', sum_f_into_x_sub_mean_raise_2)
print('summation of f(x-mean)^3 = ', sum_f_into_x_sub_mean_raise_3)
print('summation of f(x-mean)^4 = ', sum_f_into_x_sub_mean_raise_4)

print('Moments about Actual Mean:')
m1 =  sum_f_into_x_sub_mean/N
m2 =  sum_f_into_x_sub_mean_raise_2/N
m3 =  sum_f_into_x_sub_mean_raise_3/N
m4 =  sum_f_into_x_sub_mean_raise_4/N


print('m1 = ', m1)
print('m2 = ', m2)
print('m3 = ', m3)
print('m4 = ', m4)

print('skewness = ', (m3 ** 2)/(m2 ** 3))
print('kurtosis = ', (m4)/(m2 ** 2))