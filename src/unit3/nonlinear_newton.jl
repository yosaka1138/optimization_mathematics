#coding: utf-8
### juliaで１変数ニュートン法を実装

f(x) = x^3 + 5x^2 + x + 1
f_prime(x) = 3x^2 + 10x + 1
f_double_prime(x) = 6x + 10

function newton(x=2.0)
    eps = 1e-20
    while true
        dx = x
        x = x - f_prime(x) / f_double_prime(x)
        if abs(x - dx) < eps
            break
        end
        # println(x, " ", dx)
    end
    return x
end

function main()
    x = 2.0
    println("*****************************************************************")
    println("* \toptimized x\t=\t", newton(x), "\t\t*")
    println("*****************************************************************")
end

main()
