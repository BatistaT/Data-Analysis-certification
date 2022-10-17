import numpy as np

def calculate(list_test):
    
    try:
        array_test = np.array(list_test).reshape(3,3)
        # Mean códigos e calculos

        mean_axis1 = np.mean(array_test, axis=1, dtype='int32')
        mean_axis0 = np.mean(array_test, axis=0, dtype='int32')
        mean_flat = np.mean(np.array(list_test), dtype='int32')
        mean_list = [mean_axis1.tolist(),mean_axis0.tolist(),mean_flat.tolist()]

        # Variance calculos

        variance_axis1 = np.var(array_test, axis=1).round(4)
        variance_axis0 = np.var(array_test, axis=0).round(4)
        variance_flat = np.var(np.array(list_test)).round(4)
        variance_list = [variance_axis1.tolist(), variance_axis0.tolist(),variance_flat.tolist()]

        # standard deviation códigos e calculos

        std_axis1 = np.std(array_test, axis=1).round(4)
        std_axis0 = np.std(array_test, axis=0).round(4)
        std_flat = np.std(np.array(list_test)).round(4)
        std_list = [std_axis1.tolist(), std_axis0.tolist(), std_flat.tolist()]

        # min calculos

        min_axis1 = np.min(array_test, axis=1)
        min_axis0 = np.min(array_test, axis=0)
        min_flat = np.min(np.array(list_test))
        min_list = [min_axis1.tolist(), min_axis0.tolist(), min_flat.tolist()]

        # max calculos

        max_axis1 = np.max(array_test, axis=1)
        max_axis0 = np.max(array_test, axis=0)
        max_flat = np.max(np.array(list_test))
        max_list = [max_axis1.tolist(), max_axis0.tolist(), max_flat.tolist()]

        # Sum calculos

        sum_axis1 = np.sum(array_test, axis=1)
        sum_axis0 = np.sum(array_test, axis=0)
        sum_flat = np.sum(np.array(list_test))
        sum_list = [sum_axis1.tolist(), sum_axis0.tolist(), sum_flat.tolist()]

        # criação de dicionario

        stats = {
            'mean': mean_list,
            'variance': variance_list,
            'standard deviation': std_list,
            'min': min_list,
            'max': max_list,
            'sum': sum_list,
        }

        print('Matrix:' '\n', array_test, '\n')
        print('Order of values: Rows / Columns / Flattened''\n')
        for key, values in stats.items():
            print(key,':', values)

    except ValueError:
            print('List must contain nine numbers') 
