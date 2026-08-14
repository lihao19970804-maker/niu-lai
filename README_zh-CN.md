# VigilMesh

**面向持续监控、定时研究、事件驱动告警和结构化报告的早期开源 Agent
运行时。**

[English](README.md) · [路线图](ROADMAP.md) · [参与贡献](CONTRIBUTING.md)

> **项目阶段：** VigilMesh v0.1.0 是可运行原型。核心 Pipeline、触发器
> 抽象、扩展接口、示例和测试已经可用；持久化调度、生产级安全控制和真实
> Provider 集成仍在规划中，请勿把当前版本视为生产就绪软件。

VigilMesh 关注的是“对话结束后仍持续运行”的 Agent。它把数据源观测转化为
一条明确、可检查的流程：

```text
collect -> analyze -> decide -> report -> alert
```

每个阶段都可以替换，并记录执行状态与耗时，便于长期运行 Agent 的配置、
扩展、调试和审计。

## 核心特点

- **默认可观察：** 每次运行都有唯一 ID、UTC 时间戳、阶段耗时以及
  `ok`、`skipped`、`error` 状态。
- **配置驱动：** 参考 CLI 可以从一个适合版本管理的小型配置文件构建
  Pipeline。
- **Provider 可扩展：** 实现 `Provider` 协议即可接入公开 API、RSS、遥测、
  数据库、Gateway 或平台适配器。
- **支持定时与事件：** `EventTrigger`、`IntervalTrigger` 和轻量调度器使用
  同一触发器约定。
- **结构化输出：** 报告同时包含易读文本和机器可读数据，告警投递是独立
  适配器。
- **安全示例：** 市场、新闻和安全监控示例只使用模拟或虚构输入，不需要
  任何凭据。

## 快速开始

需要 Python 3.9 或更高版本，运行时没有第三方依赖。

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
vigilmesh run --config configs/example.yaml
```

输出机器可读 JSON：

```bash
vigilmesh run --config examples/news_monitor/config.yaml --json
```

v0.1.0 的 `.yaml` 示例采用 JSON 兼容的 YAML 语法，从而保持零依赖；完整
YAML 加载能力已列入路线图。

## 运行模型

| 阶段 | 接口 | 职责 |
| --- | --- | --- |
| collect | `Provider` | 从数据源获得规范化观测 |
| analyze | `Analyzer` | 提取信号并生成有限区间分数 |
| decide | `Decider` | 决定动作以及是否告警 |
| report | `Reporter` | 生成面向人和机器的报告 |
| alert | `Alerter` | 通过可替换通道投递告警 |

`Tool` 和 `Registry` 提供复用 Agent 能力的首个扩展点，`Scheduler` 把
Pipeline 与定时或事件触发器连接。项目仍处于早期阶段，接口保持小而明确，
方便根据真实集成反馈演进。

## 示例说明

- `examples/market_monitor`：模拟的公开市场信号，不是交易系统，也不构成
  投资建议。
- `examples/news_monitor`：虚构的公开新闻研究输入。
- `examples/security_monitor`：合成安全遥测，不执行扫描或修复命令。

## 测试

```bash
python -m unittest discover -s tests -v
python -m compileall -q src tests
```

GitHub Actions 会在 Python 3.9 和 3.12 上运行相同检查。

## 安全与隐私

请勿提交 API key、token、cookie、SSH 材料、私人账户数据、持仓或个人配置。
从 `.env.example` 开始，并把真实值保存在仓库之外。安全报告方式及当前原型
限制见 [SECURITY.md](SECURITY.md)。

## 参与贡献

欢迎围绕 Provider 接口、持久化调度、幂等、告警适配器、可观察性和入门文档
提交聚焦的 Issue 与小型 Pull Request。提交前请阅读
[CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

[MIT](LICENSE)
