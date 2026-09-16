"""Same two-tank chart fixture as JSPT tests/contracts/test_chart_law.py."""
from __future__ import annotations

import numpy as np

from set_lcm.coordinates import AffineCoordinates
from set_lcm.invariant import GaussianState, predict, update

F = np.array([[0.96, 0.03], [0.04, 0.97]])
DRIFT = np.array([0.2, -0.2])
Q = 0.01 * np.array([[1.0, -1.0], [-1.0, 1.0]])
H = np.eye(2)
OFFSET = np.array([0.7, -0.4])
R = np.array([[0.25, 0.08], [0.08, 0.36]])
MEAN = np.array([40.0, 60.0])
P = np.array([[1.0, 0.2], [0.2, 1.5]])
Z = np.array([40.9, 59.6])


def test_two_tank_chart_restores_posterior_and_nis():
    state = GaussianState(MEAN, P)
    chart = AffineCoordinates(np.diag([1000.0, 1000.0]), [0.0, 100.0])
    native_prior = predict(state, F, DRIFT, Q)
    native = update(native_prior, Z, H, R, OFFSET)
    f_p, d_p, q_p = chart.transform_dynamics(F, DRIFT, Q)
    h_p, a_p = chart.transform_observation(H, OFFSET)
    primed_prior = predict(chart.transform_state(state), f_p, d_p, q_p)
    primed = update(primed_prior, chart.matrix @ Z + chart.offset, h_p, R * 1e6, a_p)
    restored = chart.restore_state(primed.posterior)
    np.testing.assert_allclose(restored.mean, native.posterior.mean, atol=1e-11, rtol=1e-11)
    np.testing.assert_allclose(restored.covariance, native.posterior.covariance, atol=1e-11, rtol=1e-11)
    np.testing.assert_allclose(primed.statistic, native.statistic, atol=1e-11, rtol=1e-11)
