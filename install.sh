#!/bin/bash

printf "#!/bin/bash\n\n${PWD}/execute.sh \"\${@}\"" > ${HOME}/.local/bin/scriptmaker && \
chmod +x ${HOME}/.local/bin/scriptmaker
