# Check Recipes

Checks the agent can write around the user's implementation. They test the idea, not the user's exact code, so they stay valid whatever approach the user takes.

## ML and Numerical Code

**Shape contract.** Assert shapes at the boundary before checking values.

```python
B, T, d = 2, 4, 8
out = attention(q, k, v)
assert out.shape == (B, T, d), out.shape
```

**Hand-computable input.** Pick inputs whose answer is obvious. If every key is identical, attention weights are uniform, so each output row is the mean of the values.

```python
q = np.random.randn(1, 3, 4)
k = np.ones((1, 3, 4))
v = np.random.randn(1, 3, 4)
np.testing.assert_allclose(attention(q, k, v), np.broadcast_to(v.mean(axis=1, keepdims=True), v.shape))
```

**Initial loss.** An untrained classifier over `C` classes should start near `ln(C)`: about 2.30 for 10 classes and 3.30 for 27 characters. A much higher value points to bad initialization or a wrong loss.

**Finite-difference gradient check.** Compare a hand-written backward pass against numerical gradients. Use float64 and a scalar loss.

```python
def numeric_grad(f, x, eps=1e-6):
    grad = np.zeros_like(x)
    for i in np.ndindex(x.shape):
        orig = x[i]
        x[i] = orig + eps
        plus = f(x)
        x[i] = orig - eps
        minus = f(x)
        x[i] = orig
        grad[i] = (plus - minus) / (2 * eps)
    return grad

def rel_error(a, b):
    return np.abs(a - b).max() / max(1e-12, np.abs(a).max() + np.abs(b).max())

assert rel_error(analytic_grad, numeric_grad(loss_fn, w)) < 1e-6
```

**Overfit one batch.** A correct model, loss, and optimizer can drive the loss on a single small batch close to zero. If it cannot, the bug is in the wiring, not the data or model size.

```python
x, y = next(iter(loader))
for step in range(500):
    loss = loss_fn(model(x), y)
    opt.zero_grad()
    loss.backward()
    opt.step()
print(loss.item())
```

**Match the reference.** Run the same seeded inputs through the user's version and the production implementation.

```python
import torch
import torch.nn.functional as F

torch.manual_seed(0)
q, k, v = (torch.randn(2, 4, 8) for _ in range(3))
mask = torch.tril(torch.ones(4, 4, dtype=torch.bool))  # True means "may attend"
torch.testing.assert_close(my_attention(q, k, v, mask), F.scaled_dot_product_attention(q, k, v, attn_mask=mask))
```

## Systems Code

**Race detector, repeated.** The detector only reports races that actually happen during a run, so repeat the tests.

```bash
go test -race -count=50 ./...
```

**Deterministic tests.** Inject time and randomness (`now func() time.Time`, a seeded `rand.Rand`) so a failure can be replayed exactly.

**Crash injection.** For logs and storage such as a WAL: write N records, truncate the file at a random byte offset to simulate a torn write, reopen, and assert that recovery returns a prefix of what was written and never a corrupt record. Run it across many offsets.

**Invariants after every operation.** Assert the property the structure promises after each step: the heap property holds, a load balancer's assigned counts sum to the total, a rate limiter never allows more than capacity in any window.

**Fuzzing.** Let Go generate inputs for parsers, decoders, and encoders, with a round-trip property such as `decode(encode(x)) == x`.

```bash
go test -fuzz=FuzzDecode -fuzztime=30s
```

**Differential test against the reference.** Apply the same random sequence of operations to the user's version and a production implementation (`container/heap`, a well-known LRU library, the standard `net/http` behavior) and compare results after each step.
