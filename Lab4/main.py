import lcg as lcg
import lfsr as lfsr
import WichmanHill as Wichman_Hill
import tests as test

def __init__():
    st = True
    while st:
        print("\n***NIST TESTS***")
        print("\n 1.LCG  \n 2.LFSR  \n 3.Wichman-Hill \n 4.SALIR\n")
        opt = int(input("Elija el metodo que desea testear: " ))

        if opt == 1:

            length = int(input("Ingrese el tamaño de la lista: "))
            bits = lcg.LCG(length)

            bitchain = []

            for i in bits:
                bitchain.append(int(i))


            print("\n***RESULTADOS DE TESTS EN LCG***\n")
            t = test.maurers_universal_test(bitchain)
            t1 = test.dft_test(bitchain)
            t2 = test.frequency_within_block_test(bitchain)
            t3 = test.longest_run_ones_in_a_block_test(bitchain)
            t4 = test.monobit_test(bitchain)
            t5 = test.runs_test(bitchain)
            t6 = test.random_excursion_test(bitchain)
            t7 = test.random_excursion_variant_test(bitchain)
            t8 = test.binary_matrix_rank_test(bitchain)
            t9 = test.serial_test(bitchain)
            
            print("TESTS RESULTS: \nTest 1:",t,"\nTest 2:",t1,"\nTest 3:",t2,"\nTest 4:",t3,"\nTest 5:",t4,"\nTest 6:",t5,"\nTest 7:",t6,"\nTest 8:",t7,"\nTest 9:",t8,"\nTest 10:",t9)
            


        if opt == 2:

            length = int(input("Ingrese el tamaño de la lista: "))
            bits = lfsr.lfsr(9, [4, 2, 5], 6)

            bitchain = []

            for i in bits:
                bitchain.append(int(i))


            print("\n***RESULTADOS DE TESTS EN LFSR***\n")
            t = test.maurers_universal_test(bitchain)
            t1 = test.dft_test(bitchain)
            t2 = test.frequency_within_block_test(bitchain)
            t3 = test.longest_run_ones_in_a_block_test(bitchain)
            t4 = test.monobit_test(bitchain)
            t5 = test.runs_test(bitchain)
            t6 = test.random_excursion_test(bitchain)
            t7 = test.random_excursion_variant_test(bitchain)
            t8 = test.binary_matrix_rank_test(bitchain)
            t9 = test.serial_test(bitchain)
            
            print("TESTS RESULTS: \nTest 1:",t,"\nTest 2:",t1,"\nTest 3:",t2,"\nTest 4:",t3,"\nTest 5:",t4,"\nTest 6:",t5,"\nTest 7:",t6,"\nTest 8:",t7,"\nTest 9:",t8,"\nTest 10:",t9)



        if opt == 3:
            bits = input("Ingrese el tamaño de la lista: ")

            bitchain = []

            for i in bits:
                bitchain.append(int(i))


            print("\n***RESULTADOS DE TESTS EN LFSR***\n")
            t = test.maurers_universal_test(bitchain)
            t1 = test.dft_test(bitchain)
            t2 = test.frequency_within_block_test(bitchain)
            t3 = test.longest_run_ones_in_a_block_test(bitchain)
            t4 = test.monobit_test(bitchain)
            t5 = test.runs_test(bitchain)
            t6 = test.random_excursion_test(bitchain)
            t7 = test.random_excursion_variant_test(bitchain)
            t8 = test.binary_matrix_rank_test(bitchain)
            t9 = test.serial_test(bitchain)
            
            print("TESTS RESULTS: \nTest 1:",t,"\nTest 2:",t1,"\nTest 3:",t2,"\nTest 4:",t3,"\nTest 5:",t4,"\nTest 6:",t5,"\nTest 7:",t6,"\nTest 8:",t7,"\nTest 9:",t8,"\nTest 10:",t9)

            
    
        if opt == 4:
            print("\n***** FIN DEL PROGRAMA *****\n")
            st = False
        if opt<1 or opt>4:
            print("\nOpción no valida, intente de nuevo\n")

if __name__ == "__main__":
    __init__()