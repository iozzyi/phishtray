import React from 'react';
import styled, { css } from 'react-emotion';
import { Checkbox } from 'carbon-components-react';
import format from 'date-fns/format';

const Row = styled('tr')({
  '&:nth-child(even) td': {
    backgroundColor: '#f4f7fb',
  },
});

const Cell = styled('td')({
  fontSize: 20,
  fontWeight: 400,
  color: '#8897a2',
  padding: '22px 0',
  verticalAlign: 'middle',
  '& .bx--form-item.bx--checkbox-wrapper': {
    marginTop: 0,
  },
});

export default function FileListItem({
  file,
  deleteFileHandler,
  displayFileModalHandler,
}) {
  const checkboxId = `checkbox-file-${file.id}`;
  return (
    <Row>
      <Cell
        className={css({ paddingLeft: 20 })}
        onClick={() => displayFileModalHandler(file.fileUrl)}
      >
        <Checkbox
          defaultChecked={false}
          indeterminate={true}
          id={checkboxId}
          className={css({ fontSize: 20, fontWeight: 500, color: '#8897a2' })}
          labelText={file.fileName || file.filename || ''}
        />
      </Cell>
      <Cell>{file.description}</Cell>
      <Cell>{format(file.dateCreated, 'DD/MM/YYYY')}</Cell>
      <Cell>
        <a
          onClick={() => deleteFileHandler(file)}
          className={css({
            fontSize: 16,
            fontWeight: 400,
            textDecoration: 'none',
            color: '#5596e6',
            cursor: 'pointer',
          })}
        >
          Delete
        </a>
      </Cell>
    </Row>
  );
}
