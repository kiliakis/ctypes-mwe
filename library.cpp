extern "C" {

    double mean_f64(const double * __restrict__ data, const int n)
    {
        double m = 0;
        for (int i = 0; i < n; ++i) {
            m += data[i];
        }
        return m / n;
    }

    void add_vector_f64(const double * __restrict__ a,
                       const double * __restrict__ b,
                       const int size,
                       double * __restrict__ result)
    {
        for (int i = 0; i < size; ++i) {
            result[i] = a[i] + b[i];
        }
    }
}