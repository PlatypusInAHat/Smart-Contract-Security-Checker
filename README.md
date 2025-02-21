# SmartContractSecurityChecker
Công cụ kiểm tra lỗ hổng bảo mật trong smart contract sử dụng Slither, Mythril, Echidna, Oyente và Securify.
## Cài đặt
1. Cài Python 3.8+.
2. Cài thư viện: `pip install -r requirements.txt`.
3. Cài Docker và chạy:
   - Oyente: `docker pull luongnguyen/oyente`
4. Cài Echidna: [Hướng dẫn](https://github.com/crytic/echidna).
5. (Tùy chọn) Cài `truffle-flattener`: `npm install -g truffle-flattener`.
## Sử dụng
Quét tất cả hợp đồng trong `contracts/`:
```bash
python src/main.py
```
Kết quả lưu trong `reports/analysis_report.md`. Log chi tiết trong `analysis.log`.
## Tính năng
- Hỗ trợ hợp đồng phức tạp cho Securify bằng cách làm phẳng tự động.
- Xóa file tạm sau phân tích.
