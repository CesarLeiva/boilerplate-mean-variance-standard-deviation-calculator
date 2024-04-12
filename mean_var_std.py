import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    else:
        list = np.array(list).reshape(3,3)
        t_list = np.transpose(list)
        calculations = {
            'mean': [[np.mean(t_list[0]), np.mean(t_list[1]), np.mean(t_list[2])], [np.mean(list[0]), np.mean(list[1]), np.mean(list[2])], np.mean(list)],
            'variance': [[np.var(t_list[0]), np.var(t_list[1]), np.var(t_list[2])], [np.var(list[0]), np.var(list[1]), np.var(list[2])], np.var(list)],
            'standard deviation': [[np.std(t_list[0]), np.std(t_list[1]), np.std(t_list[2])], [np.std(list[0]), np.std(list[1]), np.std(list[2])], np.std(list)],
            'max': [[np.max(t_list[0]), np.max(t_list[1]), np.max(t_list[2])], [np.max(list[0]), np.max(list[1]), np.max(list[2])], np.max(list)],
            'min': [[np.min(t_list[0]), np.min(t_list[1]), np.min(t_list[2])], [np.min(list[0]), np.min(list[1]), np.min(list[2])], np.min(list)],
            'sum': [[np.sum(t_list[0]), np.sum(t_list[1]), np.sum(t_list[2])], [np.sum(list[0]), np.sum(list[1]), np.sum(list[2])], np.sum(list)]
        }
        return calculations