from tqdm import tqdm
from multiprocessing import Pool, cpu_count

# мультипроцесорная обработка заданий
# jobs = array[param_for_job]
def job_worker(jobs, job_function, tqdm_label='jobs', processes=0):
    if processes==0: processes = cpu_count()-1
    results = []
    with Pool(processes=processes) as pool:
        with tqdm(tqdm_label, total=len(jobs)) as pbar:
            for value in pool.imap_unordered(job_function, jobs):
                results.append(value)
                pbar.update()
        return results