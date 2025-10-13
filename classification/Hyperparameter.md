

**4.2. Key parameters**


Several key hyper-parameters are specified. For the coefficient α1, in Eq. 1, which controls the trade-off between maintaining the model's performance and embedding the watermark effectively. Here α1, is set to 1.2, with the optimal range being 1.0 to 1.5. For the hinge margin θ in Eq. 2, we set θ = 0.01. The lengths of the watermark n can be set to 32, 48, 64, 96, 128 and 256. The number of masks s is set to 260, with the optimal range being 250–300. When only a few masked samples are available, it is difficult to accurately assess the significance of each basic part, resulting in unsatisfactory feature impact analysis. For the ridge parameter τ in Eq. 4, it is typically set to a small positive value, such as within the range τ ∈ [10−3, 10−1] , which helps prevent the matrix MT M from being singular or numerically unstable while avoiding excessive smoothing of feature importance. In our work, the default setting is τ = 0.01.
















