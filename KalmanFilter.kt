class KalmanFilter(private val R: Float,
                   private val Q: Float,
                   private val A: Float = 1.0f,
                   private val B: Float = 0.0f,
                   private val C: Float = 1.0f) {

    private var x: Float? = null
    private var cov: Float = 0.0f

    private fun square(x: Float) = x * x

    private fun predict(x: Float, u: Float): Float = (A * x) + (B * u)

    private fun uncertainty(): Float = (square(A) * cov) + R

    fun filter(signal: Float, u: Float = 0.0f): Float {
        val x = this.x

        if (x == null) {
            this.x = (1 / C) * signal
            cov = square(1 / C) * Q
        } else {
            val prediction = predict(x, u)
            val uncertainty = uncertainty()

            // kalman gain
            val k_gain = uncertainty * C * (1 / ((square(C) * uncertainty) + Q))

            // correction
            this.x = prediction + k_gain * (signal - (C * prediction))
            cov = uncertainty - (k_gain * C * uncertainty)
        }

        return this.x!!
    }
}