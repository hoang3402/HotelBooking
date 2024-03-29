# các chức năng:

- **Chức năng của Người dùng**:
    - [x] Tạo tài khoản (tên, số điện thoại, và email)
    - [ ] Xem danh sách khách sạn
        - Có nhiều khách sạn trong hệ thống
        - Thông tin cơ bản về từng khách sạn, bao gồm tên, địa chỉ và giá cả theo loại phòng
    - [ ] Tìm kiếm khách sạn
        - Có thể tìm kiếm theo tiêu chí như địa điểm (tên phòng, thành phố, tỉnh...), ngày nhận phòng, ngày trả phòng,
          và số lượng người.
        - Người dùng xem được số lượng các khách sạn thoã mãn những tiêu chí nhất định
    - [ ] Xem Chi tiết khách sạn
        - Khi người dùng chọn một khách sạn từ danh sách tìm kiếm, họ có thể xem thông tin chi tiết về từng khách sạn.
        - Thông tin chi tiết bao gồm mô tả, hình ảnh, tiện nghi, giá cả, và thông tin về các loại phòng có sẵn
    - [ ] Đặt Phòng
        - cần chọn ngày nhận phòng, ngày trả phòng, số lượng người, và loại phòng
    - [ ] Xác nhận Đặt Phòng
        - Sau khi hoàn thành việc đặt phòng, hệ thống sẽ xác nhận đặt phòng và gửi thông tin phiếu xác nhận đặt phòng
          đến email của người dùng đã đăng ký.
          Thông tin trong phiếu xác nhận bao gồm chi tiết về đặt phòng và thông tin liên hệ của khách sạn.
    - [ ] Quản lý đặt phòng
        - Xem, huỷ đặt phòng hiện tại
    - [ ] Xem lịch sử đặt phòng
        - Lịch sử đặt phòng bao gồm thông tin về các đặt phòng hiện tại và các đặt phòng trước đây mà họ đã thực hiện.
    - [ ] Đánh giá
        - Có thể đánh giá, comment cho khách sạn họ đã lưu trú


- **Chức năng của Quản trị viên**:
    - [ ] Quản lý lịch đặt phòng
        - [ ] Xem và quản lý việc đặt phòng
        - Bao gồm xác nhận đặt phòng, hủy bỏ đặt phòng, và sửa đổi thông tin đặt phòng.


- **Chức năng của Quản trị viên Super Admin**:
    - [ ] Quản lý Ứng dụng
        - Quản trị viên có khả năng quản lý người dùng (thêm, xóa, sửa, tìm kiếm người dùng)
        - Có thể xem toàn bô khách sạn, phòng trong hệ thống


- [ ] **Chức năng Tích hợp Thanh toán**:
    - Cung cấp tích hợp đơn giản với cổng thanh toán để xử lý thanh toán cho đặt phòng.
    - Kế hoạch sẽ sử dụng VNPay


- [ ] **Chức năng Hỗ trợ Trực tuyến**:
    - Cung cấp chatbot để hỗ trợ người dùng về việc đặt phòng hoặc giải quyết sự cố.

---

# Setup docker

---

## python

command make requirements
```shell
pip freeze > requirements.txt
```

```shell
py manage.py makemigrations
```

```shell
py manage.py migrate
```