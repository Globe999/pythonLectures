import matplotlib.pyplot as plt
import numpy as np

def logmap(r, x):
    return r*x*(1-x)
    
def attractors(r,x,n,epsilon):
    num_list = []
    att_list = []
    ans = x
    for _ in range(n):
        ans = logmap(r,ans)
        if len(att_list) < 1:
            for num in num_list:
                if abs(ans-num) < epsilon:
                    att_list.append(ans)
        else:
            if abs(ans-att_list[0]) < epsilon:
                return att_list
            else:
                att_list.append(ans)
        num_list.append(ans)

def main():
    
    bifurcationDiagram(0)

def bifurcationDiagram(r_val):
    x_val = []
    y_val = []

    while r_val <= 3.9:
        list = attractors(r_val, 0.2, 100, 1e-5)
        if list:
            for i in list:
                x_val.append(r_val)
                y_val.append(i)
        r_val += 0.003

    plt.scatter(x_val, y_val, color="red", s=0.5, label="dot")
	# plt.xlabel('ages')
	# plt.ylabel('sal')
    plt.title('ages and sals')

    plt.legend()
    plt.show()

main()