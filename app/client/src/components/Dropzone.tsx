import React, { useCallback, useState } from "react";
import { useDropzone, FileWithPath } from "react-dropzone";
import "./dropzone.css";

const Dropzone: React.FC = () => {
  const [file, setFile] = useState<FileWithPath>(null);

  const onDrop = useCallback((acceptedFiles: FileWithPath[]) => {
    const reader = new FileReader();

    reader.onabort = () => console.log("file reading was aborted");
    reader.onerror = () => console.log("file reading has failed");
    reader.onload = () => {
      const binaryStr = reader.result;
      console.log(binaryStr);
      // TODO: send request to backend with image
    };
    reader.readAsArrayBuffer(acceptedFiles[0]);
    setFile(acceptedFiles[0]);
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
    <div>
      <div {...getRootProps()} className="dropzone-container">
        <input {...getInputProps()} className="dropzone-input" />
        {isDragActive ? (
          <p>Drop the files here ...</p>
        ) : (
          <p>Drag 'n' drop some files here, or click to select files</p>
        )}
      </div>
      <div className="dropped-files">
        {file ? (
          <div className="file-item">
            <p>{file.path}</p>
          </div>
        ) : (
          ""
        )}
      </div>
    </div>
  );
};

export default Dropzone;
