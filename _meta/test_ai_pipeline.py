#!/usr/bin/env python3
"""
端到端测试：AI 增强 PDF 处理流程
"""
import os
import sys
import tempfile
from pathlib import Path

# 添加 _meta 到路径
sys.path.insert(0, str(Path(__file__).parent))

from ai_enhancer import KimiEnhancer

# 测试用的模拟 PDF 提取文本
TEST_PAPER_TEXT = """
Title: Deep learning predicts gene expression from chromatin accessibility

Abstract:
Understanding the relationship between chromatin accessibility and gene 
expression is fundamental to decoding gene regulation. Here we present 
AtacWorks, a deep convolutional neural network approach that predicts 
chromatin accessibility from ATAC-seq data, even from low-cell-number 
or low-coverage experiments. AtacWorks denoises and identifies regulatory 
elements from noisy accessibility data, outperforming existing methods. 
We applied AtacWorks to single-cell ATAC-seq data from human blood cells 
and identified cell-type-specific enhancers and transcription factor motifs.

Introduction:
Gene expression is regulated by chromatin accessibility, which determines 
which regulatory elements are available for transcription factors to bind. 
ATAC-seq is the standard method for measuring chromatin accessibility, but 
requires thousands of cells and produces noisy data at low coverage.

Methods:
- Deep convolutional neural network (CNN) with residual connections
- ATAC-seq data from GM12878, K562, and H1 cell lines
- Single-cell ATAC-seq from 10x Genomics platform
- Training on 50 million genomic windows
- Adam optimizer, learning rate 1e-4, batch size 64

Results:
AtacWorks achieved Pearson correlation of 0.95 between predicted and 
measured accessibility, compared to 0.72 for baseline methods. On 
single-cell data, AtacWorks identified 15,000 cell-type-specific peaks 
with 85% precision. Key transcription factors identified: GATA1 in 
erythroid cells, PU.1 in myeloid cells, and TCF7 in T cells.

Discussion:
AtacWorks enables high-quality chromatin accessibility analysis from 
limited input material. The approach is generalizable to other epigenomic 
assays and could accelerate studies of gene regulation in rare cell 
populations and clinical samples.
"""

def test_end_to_end():
    """测试端到端 AI 精炼"""
    print("=" * 70)
    print("端到端 AI 增强测试")
    print("=" * 70)
    
    # 设置 API Key
    api_key = os.environ.get("KIMI_API_KEY")
    if not api_key:
        print("错误: KIMI_API_KEY 环境变量未设置")
        sys.exit(1)
    
    # 创建 Enhancer
    enhancer = KimiEnhancer(
        api_key=api_key,
        model="8k",  # 使用 8k 模型（文本较短）
        verbose=True
    )
    
    print("\n1. 测试论文精炼...")
    result = enhancer.enhance_paper(TEST_PAPER_TEXT, title="AtacWorks")
    
    print(f"\n2. 结果验证:")
    print(f"   成功: {result.success}")
    print(f"   置信度: {result.confidence}")
    print(f"   模型: {result.model_used}")
    print(f"   Tokens: {result.tokens_used}")
    
    print(f"\n3. 提取的标题:")
    print(f"   {result.title}")
    
    print(f"\n4. 摘要:")
    print(f"   {result.abstract[:200]}...")
    
    print(f"\n5. 关键词:")
    print(f"   {', '.join(result.keywords)}")
    
    print(f"\n6. 实体:")
    for entity_type, entities in result.entities.items():
        if entities:
            print(f"   {entity_type}: {', '.join(entities[:5])}")
    
    print(f"\n7. 完整 AIMRaD 结构:")
    print(f"   - 背景: {'✓' if result.background else '✗'} ({len(result.background)} 字符)")
    print(f"   - 发现: {'✓' if result.findings else '✗'} ({len(result.findings)} 字符)")
    print(f"   - 方法: {'✓' if result.methods else '✗'} ({len(result.methods)} 字符)")
    print(f"   - 讨论: {'✓' if result.discussion else '✗'} ({len(result.discussion)} 字符)")
    
    print(f"\n8. 统计:")
    print(f"   {enhancer.get_stats()}")
    
    # 验证质量
    print(f"\n9. 质量检查:")
    checks = [
        ("标题非空", bool(result.title)),
        ("摘要非空", len(result.abstract) > 50),
        ("关键词数量", len(result.keywords) >= 3),
        ("背景非空", len(result.background) > 20),
        ("发现非空", len(result.findings) > 20),
        ("方法非空", len(result.methods) > 20),
        ("讨论非空", len(result.discussion) > 20),
    ]
    
    all_passed = True
    for check_name, passed in checks:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"   {status}: {check_name}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 70)
    if all_passed:
        print("✓ 所有检查通过！AI 增强功能正常工作。")
    else:
        print("✗ 部分检查失败，可能需要调整 prompt 模板。")
    print("=" * 70)
    
    return all_passed

if __name__ == "__main__":
    success = test_end_to_end()
    sys.exit(0 if success else 1)
