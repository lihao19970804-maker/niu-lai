# 牛来 (NiuLai)

**An early-stage, open-source agent runtime for continuous monitoring,
scheduled research, event-driven alerts, and structured reports.**

[简体中文](README_zh-CN.md) · [Roadmap](ROADMAP.md) · [Contributing](CONTRIBUTING.md)

> **Project status:** 牛来 (NiuLai) v0.1.0 is a functional prototype. The core
> pipeline, trigger abstractions, extension interfaces, examples, and tests run
> today; durable scheduling, production security controls, and real provider
> integrations are planned. Do not treat it as production-ready yet.

用了牛来，股市就牛来啦。这个口号是轻松的项目记忆点，不是收益承诺；牛来不
构成投资建议，市场监控仅作为公开或模拟数据示例。

牛来 (NiuLai) is for agents that keep watch after an interactive chat ends. It
turns data-source observations into an explicit, inspectable sequence:

```text
collect -> analyze -> decide -> report -> alert
```

The runtime keeps each stage replaceable and records its status and duration.
That makes a long-running agent easier to configure, extend, debug, and audit
than a single opaque loop.

## Why 牛来

- **Observable by default:** every run has a unique ID, UTC timestamps,
  per-stage timing, and explicit `ok`, `skipped`, or `error` state.
- **Configuration-led:** the reference CLI builds a useful pipeline from a
  small, versionable configuration file.
- **Provider-neutral:** implement the `Provider` protocol for public APIs,
  RSS, telemetry, databases, gateways, or platform adapters.
- **Event and schedule ready:** `EventTrigger`, `IntervalTrigger`, and a small
  scheduler share one trigger contract.
- **Structured outputs:** reports contain both readable text and machine-ready
  data; alert delivery is a separate adapter.
- **Safe examples:** the bundled market, news, and security monitors use only
  simulated or fictional inputs and no credentials.

## Quickstart

牛来 requires Python 3.9 or newer and has no runtime dependencies. The Python
package and CLI remain `vigilmesh` in v0.1.0 for compatibility.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
vigilmesh run --config configs/example.yaml
```

For machine-readable output:

```bash
vigilmesh run --config examples/news_monitor/config.yaml --json
```

The `.yaml` examples use JSON-compatible YAML syntax so v0.1.0 stays
dependency-free. A full YAML loader is on the roadmap.

## Minimal Python usage

```python
from vigilmesh.config import load_config
from vigilmesh.factory import build_pipeline

config = load_config("configs/example.yaml")
result = build_pipeline(config).run({"trigger": "manual"})
print(result.report.body)
```

## Runtime model

| Stage | Contract | Responsibility |
| --- | --- | --- |
| collect | `Provider` | Obtain normalized observations from a source |
| analyze | `Analyzer` | Extract signals and a bounded score |
| decide | `Decider` | Select an action and whether to alert |
| report | `Reporter` | Produce human- and machine-readable output |
| alert | `Alerter` | Deliver an alert through a replaceable channel |

`Tool` and `Registry` provide the first extension seam for reusable agent
capabilities. `Scheduler` connects pipelines to either interval or event
triggers. These interfaces are intentionally small while the project gathers
real integration feedback.

## Examples

- `examples/market_monitor`: synthetic public-market signals. It is not a
  trading system and does not contain investment advice.
- `examples/news_monitor`: fictional public-news research input.
- `examples/security_monitor`: synthetic security telemetry with no scans or
  remediation commands.

## Testing

```bash
python -m unittest discover -s tests -v
python -m compileall -q src tests
```

GitHub Actions runs the same checks on Python 3.9 and 3.12.

## Security and privacy

Never commit API keys, tokens, cookies, SSH material, private account data,
holdings, or personal configuration. Start from `.env.example` and keep real
values outside the repository. See [SECURITY.md](SECURITY.md) for reporting
guidance and the current prototype limitations.

## Contributing

牛来 welcomes focused issues and small pull requests, especially around
provider contracts, durable scheduling, idempotency, alert adapters,
observability, and beginner-friendly documentation. Read
[CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.

## License

[MIT](LICENSE)
