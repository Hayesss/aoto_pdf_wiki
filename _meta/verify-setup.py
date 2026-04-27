#!/usr/bin/env python3
"""
LLM-Wiki 部署验证脚本

检查项目在新环境中的可用性。
用法:
    python _meta/verify-setup.py
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path


def check(cmd, name=None):
    """检查命令是否可用"""
    name = name or cmd
    if shutil.which(cmd):
        print(f"  [OK] {name}")
        return True
    else:
        print(f"  [MISSING] {name} — 请安装后重试")
        return False


def main():
    print("=" * 50)
    print("LLM-Wiki 部署验证")
    print("=" * 50)

    ok = True

    # 1. 检查 pixi
    print("\n[1/6] 包管理器")
    ok &= check("pixi", "pixi (conda-forge 包管理)")

    # 2. 检查 Python
    print("\n[2/6] Python 环境")
    try:
        import sys
        ver = sys.version_info
        if ver >= (3, 11):
            print(f"  [OK] Python {ver.major}.{ver.minor}.{ver.micro}")
        else:
            print(f"  [WARN] Python {ver.major}.{ver.minor} — 建议 >= 3.11")
            ok = False
    except Exception as e:
        print(f"  [ERROR] 无法检测 Python: {e}")
        ok = False

    # 3. 检查核心命令
    print("\n[3/6] 外部工具")
    # marker-pdf 安装在系统 Python 3.12 中
    marker_ok = False
    try:
        result = subprocess.run(
            ["python3.12", "-c", "from marker.scripts.convert_single import convert_single_cli; print('OK')"],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            print("  [OK] marker-pdf (PDF 提取, 系统 Python 3.12)")
            marker_ok = True
        else:
            print("  [MISSING] marker-pdf (PDF 提取) — 请安装: pip3.12 install marker-pdf")
    except Exception:
        print("  [MISSING] marker-pdf (PDF 提取) — 请安装: pip3.12 install marker-pdf")
    ok &= marker_ok
    ok &= check("git", "git (版本控制)")

    # 4. 检查目录结构
    print("\n[4/6] 目录结构")
    wiki_dir = Path(__file__).parent.parent
    required_dirs = [
        "inbox", "raw/papers", "raw/articles", "raw/transcripts",
        "raw/assets", "papers", "processed", "failed",
        "_meta", "_templates", "entities", "concepts"
    ]
    for d in required_dirs:
        p = wiki_dir / d
        if p.exists():
            print(f"  [OK] {d}/")
        else:
            print(f"  [CREATE] {d}/ — 自动创建")
            p.mkdir(parents=True, exist_ok=True)

    # 5. 检查 pixi 环境
    print("\n[5/6] pixi 环境")
    pixi_toml = wiki_dir / "pixi.toml"
    if pixi_toml.exists():
        print(f"  [OK] pixi.toml 存在")
        # 尝试解析
        try:
            result = subprocess.run(
                ["pixi", "list"], cwd=wiki_dir,
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                print("  [OK] pixi 环境可解析")
            else:
                print(f"  [WARN] pixi 环境解析失败:\n{result.stderr[:200]}")
                ok = False
        except Exception as e:
            print(f"  [WARN] 无法验证 pixi 环境: {e}")
    else:
        print("  [MISSING] pixi.toml — 项目配置缺失")
        ok = False

    # 6. 检查磁盘空间
    print("\n[6/6] 磁盘空间")
    stat = shutil.disk_usage(wiki_dir)
    free_gb = stat.free / (1024**3)
    if free_gb > 5:
        print(f"  [OK] 可用空间: {free_gb:.1f} GB (marker-pdf 模型需 ~3-5GB)")
    else:
        print(f"  [WARN] 可用空间仅 {free_gb:.1f} GB — 建议至少 5GB")
        ok = False

    # 总结
    print("\n" + "=" * 50)
    if ok:
        print("验证通过！项目可以正常部署。")
        print("\n下一步:")
        print("  pixi install")
        print("  pixi run process-pdfs")
        return 0
    else:
        print("验证发现问题，请按上方提示修复后再试。")
        return 1


if __name__ == "__main__":
    sys.exit(main())
