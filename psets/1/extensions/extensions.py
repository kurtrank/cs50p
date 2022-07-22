# clean input and get final segment after last `.`
extension = input("File name: ").strip().lower().rpartition(".")[2]

# set default
mimetype = "application/octet-stream"

match extension:
    case "gif":
        mimetype = "image/gif"
    case "jpg" | "jpeg":
        mimetype = "image/jpeg"
    case "png":
        mimetype = "image/png"
    case "pdf":
        mimetype = "application/pdf"
    case "txt":
        mimetype = "text/plain"
    case "zip":
        mimetype = "application/zip"

print(mimetype)
